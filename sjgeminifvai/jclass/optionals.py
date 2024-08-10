from jnius import autoclass
from sjgeminifvai import package


RequestOptions = autoclass(f"{package}.type.RequestOptions")
