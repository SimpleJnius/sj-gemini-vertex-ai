from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod
)
from sjgeminifvai import package_path

__all__ = ("SafetySetting", )


class SafetySetting(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/SafetySetting"
    __javaconstructor__ = (
        f"(L{package_path}/type/HarmCategory;"
        f"L{package_path}/type/BlockThreshold;)V",
    )

    getHarmCategory = JavaMethod(f"()L{package_path}/type/HarmCategory;")
    getThreshold = JavaMethod(f"()L{package_path}/type/BlockThreshold;")
