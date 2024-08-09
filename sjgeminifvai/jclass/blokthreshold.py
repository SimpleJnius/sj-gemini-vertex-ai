from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticField,
    JavaStaticMethod
)
from sjgeminifvai import package_path

__all__ = ("BlockThreshold", )


class BlockThreshold(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/HarmCategory"
    UNSPECIFIED = JavaStaticMethod(f"L{package_path}/type/BlockThreshold;")
    LOW_AND_ABOVE = JavaStaticMethod(f"L{package_path}/type/BlockThreshold;")
    MEDIUM_AND_ABOVE = JavaStaticMethod(f"L{package_path}/type/BlockThreshold;")
    ONLY_HIGH = JavaStaticMethod(f"L{package_path}/type/BlockThreshold;")
    NONE = JavaStaticMethod(f"L{package_path}/type/BlockThreshold;")
    values = JavaStaticMethod(f"()[L{package_path}/type/BlockThreshold;")
    valueOf = JavaStaticMethod(
        f"(Ljava/lang/String;)"
        f"L{package_path}/type/BlockThreshold;"
    )

