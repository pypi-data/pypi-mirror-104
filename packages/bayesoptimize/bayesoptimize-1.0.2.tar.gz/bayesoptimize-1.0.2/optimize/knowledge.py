import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod, abstractclassmethod
import json

class Parameter:
    
    """A class for a model parameter.

    Attributes:
        name (str): The name of the parameter.
        value (str): The current value of the parameter.
        vary (bool): Whether or not to vary (optimize) this parameter.
        priors (list): A list of priors to apply.
        scale (float): A search scale to initiate mcmc walkers.
        latex_str (str): A string for plot formatting, most likely using latex formatting.
    """
    
    __slots__ = ['name', 'value', 'vary', 'priors', 'scale', 'latex_str', 'unc']

    def __init__(self, name=None, value=None, vary=True, priors=None, scale=None, latex_str=None, unc=None):
        """Creates a Parameter object.

        Args:
            name (str): The name of the parameter.
            value (Number): The starting value of the parameter.
            vary (bool): Whether or not to vary (optimize) this parameter.
            priors (list): A list of priors to apply.
        """
        
        # Set all attributes
        self.name = name
        self.value = value
        self.vary = vary
        if type(priors) is list:
            self.priors = priors
        elif isinstance(priors, AbstractPrior):
            self.priors = [priors]
        else:
            self.priors = []
        self.scale = scale
        self.latex_str = self.name if latex_str is None else latex_str
        self.unc = None

    def __repr__(self):
        s = f"Name: {self.name} | Value: {self.value}"
        if not self.vary:
            s += ' (Locked)'
        if self.unc is not None:
            s += f" | Unc: -{self.unc[0]}, +{self.unc[1]}"
        if len(self.priors) > 0:
            s += '\n  Priors:\n'
            for prior in self.priors:
                s += "   " + prior.__repr__() + "\n"
        return s
    
    def set_name(self, name):
        self.name = name
        if self.latex_str is None:
            self.latex_str = name
    
    def get_hard_bounds(self):
        """Gets the hard bounds from uniform priors if present, otherwise assumes +/- inf.

        Returns:
            np.ndarray: The lower bounds.
            np.ndarray: The upper bounds.
        """
        vlb, vub = -np.inf, np.inf
        if len(self.priors) > 0:
            for prior in self.priors:
                if isinstance(prior, Uniform):
                    vlb, vub = prior.minval, prior.maxval
                    return vlb, vub
        return vlb, vub
    
    def compute_crude_scale(self):
        if self.scale is not None:
            return self.scale
        if len(self.priors) == 0:
            scale = np.abs(self.value) / 100
            if scale == 0:
                return 1
            else:
                return scale
        for prior in self.priors:
            if isinstance(prior, Gaussian):
                return prior.sigma
        for prior in self.priors:
            if isinstance(prior, Uniform):
                dx1 = np.abs(prior.maxval - self.value)
                dx2 = np.abs(self.value - prior.minval)
                scale = np.min([dx1, dx2]) / 100
                if scale == 0:
                    return 1
                else:
                    return scale
        scale = np.abs(self.value) / 100
        if scale == 0:
            return 1
        else:
            return scale

    @property
    def value_str(self):
        """The current value of the parameter as a string

        Returns:
            str: The value as a string
        """
        return str(self.value)
    
    def setv(self, **kwargs):
        """Setter method for the attributes.
        
        Args:
            kwargs: Any available atrributes.
        """
        for key in kwargs:
            if key == 'name':
                self.set_name(kwargs[key])
            else:
                setattr(self, key, kwargs[key])
        
    @property
    def hard_bounds(self):
        return self.get_hard_bounds()
    
    def has_prior(self, prior_type):
        for _prior in self.priors:
            tt = type(_prior)
            if prior_type is tt:
                return True
        return False
    
    def add_prior(self, prior):
        self.priors.append(prior)
        
    def get_serializable(self):
        return {"name": self.name, "value": self.value, "vary": self.vary, "latex_str": self.latex_str, "priors": [prior.get_serializable() for prior in self.priors]}
    
    @classmethod
    def from_serialized(cls, o):
        try:
            priors = cls.from_serialized_priors(o["priors"])
            return cls(name=o["name"], value=o["value"], vary=o["vary"], latex_str=o["latex_str"], priors=priors)
        except:
            raise ValueError("Cannot parse one or more fields for Parameter object")
        
    @staticmethod
    def from_serialized_priors(serialized_priors):
        priors_list = []
        for prior in serialized_priors:
            name = prior["name"]
            if name == "Gaussian":
                priors_list.append(Gaussian.from_prior(prior))
            elif name == "Uniform":
                priors_list.append(Uniform.from_prior(prior))
            elif name == "Jeffreys":
                priors_list.append(Jeffreys.from_prior(prior))
            elif name == "Positive":
                priors_list.append(Positive.from_prior(prior))
            elif name == "Negative":
                priors_list.append(Negative.from_prior(prior))
        return priors_list
        
class Parameters(dict):
    """A container for a set of model parameters which extends the Python 3 dictionary, which is ordered by default.
    """
    
    default_keys = Parameter.__slots__

    def __init__(self):
        """Creates a Parameters object (empty dict).
        """
        
        # Initiate the actual dictionary.
        super().__init__()
            
            
    @classmethod
    def pack(cls, pdict):
        """Create a parameters object from a dict of numpy arrays
        
        Args:
            pdict (dict): A dictionary of Parameter attributes (the result from unpack).
        """
        
        pars = cls()
        n = len(pdict['value'])
        name = pdict['name']
            
        for ipname, pname in enumerate(name):
            par_kwargs = {}
            par_kwargs['name'] = pname
            par_kwargs['value'] = pdict['value'][ipname]
            for ikey, kw in enumerate(pdict):
                if pdict[kw] is not None and kw not in par_kwargs:
                    par_kwargs[kw] = pdict[kw][ipname]
            pars.add_parameter(Parameter(**par_kwargs))
        return pars
          

    def add_parameter(self, par):
        """Adds a parameter to the Parameters dictionary with par.name as a key.

        Args:
            par (Parameter): The parameter to add.
        """
        self[par.name] = par
        
    def compute_crude_scales(self):
        scales = np.array([self[pname].compute_crude_scale() for pname in self], dtype=float)
        return scales
            
    def unpack(self, keys=None, vary_only=False):
        """Unpacks values to a dict of numpy arrays.

        Args:
            keys (iterable or string): A tuple of strings containing the keys to unpack, defaults to None for all keys.
            
        Returns:
            dict: A dictionary containing the returned values.
        """
        if keys is None:
            keys = self.default_keys
        else:
            t = type(keys)
            if t is str:
                keys = [keys]
        out = {}
        if vary_only:
            for key in keys:
                t = type(getattr(self[0], key))
                out[key] = np.array([getattr(self[pname], key) for pname in self if self[pname].vary], dtype=t)
        else:
            for key in keys:
                t = type(getattr(self[0], key))
                out[key] = np.array([getattr(self[pname], key) for pname in self], dtype=t)
        return out
            
    def pretty_print(self):
        """Prints all parameters and attributes in a readable fashion.
        """
        for key in self.keys():
            print(self[key], flush=True)
    
    def setv(self, **kwargs):
        """Setter method for an attribute(s) for all parameters, in order of insertion.

        kwargs:
            Any available Parameter atrribute.
        """
        
        for key in kwargs:
            vals = kwargs[key]
            for i, pname in enumerate(self):
                setattr(self[pname], key, vals[i])

    def __setitem__(self, key, par):
        if par.name is None:
            par.setv(name=key)
        super().__setitem__(key, par)
                
    def sanity_check(self):
        """Checks for parameters which vary and are out of Uniform bounds.
            Throws:
                AssertionError: If any parameters are outside of their Uniform bounds, an error is thrown.
                
        """
        bad_pars = []
        for pname in self:
            for prior in self[pname].priors:
                if isinstance(prior, 'Prior'):
                    v = self[pname].value
                    vary = self[pname].vary
                    vlb, vub = self[pname].get_hard_bounds()
                    if (v < vlb or v > vub) and vary:
                        bad_pars.append(pname)
            
        assert len(bad_pars) == 0
    
    def num_varied(self):
        """The number of varied parameters.

        Returns:
            int: The number of varied parameters.
        """
        nv = 0
        for pname in self:
            nv += int(self[pname].vary)
        return nv
    
    def num_locked(self):
        """The number of locked parameters.

        Returns:
            int: The number of locked parameters.
        """
        nl = 0
        for pname in self:
            nl += int(not self[pname].vary)
        return nl
    
    def get_varied(self):
        """Gets the varied parameters in a new parameters object

        Returns:
            Parameters: A parameters object containing pointers to only the varied parameters.
        """
        varied_pars = Parameters()
        for pname in self:
            if self[pname].vary:
                varied_pars.add_parameter(self[pname])
        return varied_pars
    
    def get_locked(self):
        """Gets the locked parameters in a new parameters object

        Returns:
            Parameters: A parameters object containing pointers to only the locked parameters.
        """
        locked_pars = Parameters()
        for pname in self:
            if not self[pname].vary:
                locked_pars.add_parameter(self[pname])
        return locked_pars
    
    def get_subspace(self, pars):
        """Gets a subspace of parameter objects.
        
        Args:
            pars (iterable of str): An iterable of string objects (the names of the parameters to fetch).

        Returns:
            Parameters: A parameters object containing pointers to the desired parameters.
        """
        sub_pars = Parameters()
        if par_names is not None:
            for pname in par_names:
                sub_pars.add_parameter(self[pname])
        else:
            par_names = list(self.keys())
            for k in indices:
                sub_pars.add_parameter(self[par_names[k]])
        return sub_pars
    
    def par_from_index(self, k, rel_vary=False):
        """Gets the parameter at a given numerical index.

        Args:
            k (int): The numerical index.
            rel_vary (bool, optional): Whether or not this index is relative to all parameters or only varied parameters. Defaults to False.

        Returns:
            Parameter: The parameter at the given index.
        """
        if rel_vary:
            return self[list(self.get_varied().keys())[k]]
        else:
            return self[list(self.keys())[k]]
    
    def index_from_par(self, name, rel_vary=False):
        """Gets the index of a given parameter name.

        Args:
            name (str): The name of the parameter.
            rel_vary (bool, optional): Whether or not to return an index which is relative to all parameters or only varied parameters. Defaults to False.

        Returns:
            int: The numerical index of the parameter.
        """
        if rel_vary:
            return list(self.get_varied().keys()).index(name)
        else:
            return list(self.keys()).index(name)
    
    def get_hard_bounds(self):
        """Gets the hard bounds.

        Returns:
            np.ndarray: The lower bounds.
            np.ndarray: The upper bounds.
        """
        n = len(self)
        vlb = np.full(n, -np.inf)
        vub = np.full(n, np.inf)
        for i, pname in enumerate(self):
            vlb[i], vub[i] = self[pname].get_hard_bounds()
        return vlb, vub
    
    def get_hard_bounds_vary(self):
        """Gets the hard bounds, but only the varied params.

        Returns:
            np.ndarray: The lower bounds.
            np.ndarray: The upper bounds.
        """
        n = self.num_varied()
        vlb = np.full(n, -np.inf)
        vub = np.full(n, np.inf)
        i = 0
        for pname in self:
            if self[pname].vary:
                vlb[i], vub[i] = self[pname].get_hard_bounds()
                i += 1
        return vlb, vub
    
    def __getitem__(self, key):
        t = type(key)
        if t is str or t is np.str or t is np.str_:
            return super().__getitem__(key)
        elif t is int:
            return self[list(self.keys())[key]]
        
    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            return super().__getattr__(attr)
        
    def get_serializable(self):
        return [par.get_serializable() for par in self.values()]
    
    @classmethod
    def from_serialized(cls, pars):
        pars_out = cls()
        for par in pars.values():
            pars_out[par["name"]] = Parameter.from_serialized(par)
        return pars_out
 
class AbstractPrior(ABC):
    """An interface for a general prior.
    """
    
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def logprob(self, x):
        pass
    
    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractclassmethod
    def from_par(self, par):
        pass

class Gaussian(AbstractPrior):
    """A prior defined by a normal distribution.

    Attributes:
        mu (float): The center of the distribution.
        sigma (float): The stddev. of the distribution.
    """
    
    __slots__ = ['mu', 'sigma']
    name = 'Gaussian'
    
    def __init__(self, mu, sigma):
        """Constructor for a Gaussian prior.

        Args:
            mu (float): The center of the distribution.
            sigma (float): The stddev. of the distribution.
        """
        assert sigma > 0
        self.mu = mu
        self.sigma = sigma
        
    def logprob(self, x):
        return -0.5 * ((x - self.mu) / self.sigma)**2 - 0.5 * np.log((self.sigma**2) * 2 * np.pi)
    
    def __repr__(self):
        return f"{self.name}: [{self.mu}, {self.sigma}]"
    
    def get_serializable(self):
        return {"name": self.name, "mu": self.mu, "sigma": self.sigma}
    
    @classmethod
    def from_par(cls, par):
        scale = par.compute_crude_scale()
        if scale == 0:
            scale = 1
        return cls(par.value, sigma=scale)
    
    @classmethod
    def from_serialized(cls, prior):
        return cls(prior["mu"], prior["sigma"])
    
# class DualGaussian(AbstractPrior):
#     """A prior defined by the sum of two normal distributions. NOTE: This is not effectively identical to one normal distribution.

#     Attributes:
#         mu1 (float): The center of the first distribution.
#         sigma1 (float): The stddev. of the first distribution.
#         mu2 (float): The center of the second distribution.
#         sigma2 (float): The stddev. of second distribution.
#     """
    
#     __slots__ = ['mu1', 'sigma2', 'mu1', 'sigma2']
#     name = 'Gaussian'
    
#     def __init__(self, mu1, sigma1, mu2, sigma2):
#         """Constructor for a Gaussian prior.

#         Args:
#             mu1 (float): The center of the first distribution.
#             sigma1 (float): The stddev. of the first distribution.
#             mu2 (float): The center of the second distribution.
#             sigma2 (float): The stddev. of second distribution.
#         """
#         assert sigma1 > 0
#         assert sigma2 > 0
#         self.mu1 = mu1
#         self.sigma1 = sigma1
#         self.mu2 = mu2
#         self.sigma2 = sigma2
        
#     #def logprob(self, x):
#         #p1 = -0.5 * ((x - self.mu) / self.sigma)**2 - 0.5 * np.log((self.sigma**2) * 2 * np.pi)
#         #return p1
    
#     def __repr__(self):
#         return f"{self.name}: [{self.mu}, {self.sigma}]"
    
#     def get_serializable(self):
#         return {"name": self.name, "mu": self.mu, "sigma": self.sigma}
    
#     @classmethod
#     def from_par(cls, par):
#         scale = par.compute_crude_scale()
#         if scale == 0:
#             scale = 1
#         return cls(par.value, sigma=scale)
    
#     @classmethod
#     def from_serialized(cls, prior):
#         return cls(prior["mu"], prior["sigma"])

class Uniform(AbstractPrior):
    """A prior defined by hard bounds.

        Attributes:
            minval (float): The lower bound.
            maxval (float): The upper bound.
        """
    
    __slots__ = ['minval', 'maxval']
    
    name = "Uniform"
    
    def __init__(self, minval, maxval):
        """Constructor for a Uniform prior.

        Args:
            minval (float): The lower bound.
            maxval (float): The upper bound.
        """
        assert minval < maxval
        self.minval = minval
        self.maxval = maxval
        
    def logprob(self, x):
        if self.minval < x < self.maxval:
            return -1 * np.log(self.maxval - self.minval)
        else:
           return -np.inf
        
    def __repr__(self):
        return f"{self.name}: [{self.minval}, {self.maxval}]"
    
    def get_serializable(self):
        return {"name": self.name, "minval": self.minval, "maxval": self.maxval}
    
    @classmethod
    def from_par(cls, par):
        scale = par.compute_crude_scale()
        return cls(par.value - scale, par.value + scale)
    
    @classmethod
    def from_serialized(cls, prior):
        return cls(prior["minval"], prior["maxval"])

class Positive(AbstractPrior):
    """A prior to force x > 0.
    """
    
    __slots__ = []
    
    name = "Positive"
    
    def __init__(self):
        pass
        
    def logprob(self, x):
        return 0 if x > 0 else -np.inf
        
    def __repr__(self):
        return self.name
    
    @classmethod
    def from_par(cls, par):
        return cls()
    
    def get_serializable(self):
        return {"name": self.name}
    
    @classmethod
    def from_serialized(cls, prior):
        return cls()
    
class Negative(AbstractPrior):
    """A prior to force x < 0.
    """
    
    __slots__ = []
    
    name = "Negative"
    
    def __init__(self):
        pass
        
    def logprob(self, x):
        return 0 if x < 0 else -np.inf
        
    def __repr__(self):
        return self.name
    
    @classmethod
    def from_par(cls, par):
        return cls()
    
    def get_serializable(self):
        return {"name": self.name}
    
    @classmethod
    def from_serialized(cls, prior):
        return cls()
        
class Jeffreys(AbstractPrior):
    """A prior defined such that its density function is proportional to the square root of the determinant of the Fisher information matrix. Specifically, the 

        Attributes:
            minval (float): The lower bound.
            maxval (float): The upper bound.
        """
    
    __slots__ = ['minval', 'maxval', 'lognorm', 'kneeval']
    name = "Jeffreys"
    
    def __init__(self, minval, maxval, kneeval=0):
        assert minval <= maxval
        self.minval = minval
        self.maxval = maxval
        self.kneeval = kneeval
        self.lognorm = np.log(1.0 / np.log((self.maxval - self.kneeval) / (self.minval - self.kneeval)))
        
    def logprob(self, x):
        if self.minval < x < self.maxval:
            return self.lognorm - np.log(x - self.kneeval)
        else:
            return -np.inf
        
    def __repr__(self):
        return f"{self.name}: [{self.minval}, {self.kneeval}, {self.maxval}]"
    
    def get_serializable(self):
        return {"name": self.name, "minval": self.minval, "maxval": self.maxval, "kneeval": self.kneeval}
    
    @classmethod
    def from_serialized(cls, prior):
        return cls(prior["minval"], prior["maxval"], prior["kneeval"])
    
    @classmethod
    def from_par(cls, par):
        return cls(1, 10)

