from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticField,
    JavaStaticMethod
)
from sjgeminifvai import package_path

__all__ = ("HarmCategory", )


class HarmCategory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/HarmCategory"
    UNKNOWN = JavaStaticField(f"L{package_path}/type/HarmCategory;")
    HARASSMENT = JavaStaticField(f"L{package_path}/type/HarmCategory;")
    HATE_SPEECH = JavaStaticField(f"L{package_path}/type/HarmCategory;")
    SEXUALLY_EXPLICIT = JavaStaticField(f"L{package_path}/type/HarmCategory;")
    DANGEROUS_CONTENT = JavaStaticField(f"L{package_path}/type/HarmCategory;")
    values = JavaStaticMethod(f"()[L{package_path}/type/HarmCategory;")
    valueOf = JavaStaticMethod(
        f"(Ljava/lang/String;)"
        f"L{package_path}/type/HarmCategory;"
    )
