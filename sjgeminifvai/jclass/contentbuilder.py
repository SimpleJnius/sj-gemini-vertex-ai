from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod
)
from sjgeminifvai import package_path

__all__ = ("ContentBuilder", )


class ContentBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/Content$Builder"
    getRole = JavaMethod("()Ljava/lang/String;")
    setRole = JavaMethod("(Ljava/lang/String;)V")
    getParts = JavaMethod("()Ljava/util/List;")
    setParts = JavaMethod("(Ljava/util/List;)V")
    addPart = JavaMethod(
        f"(L{package_path}/type/Part;)"
        f"L{package_path}/type/Content$Builder;"
    )
    addText = JavaMethod(
        f"(Ljava/lang/String;)"
        f"L{package_path}/type/Content$Builder;"
    )
    addBlob = JavaMethod(
        "(Ljava/lang/String;[B)"
        f"L{package_path}/type/Content$Builder;"
    )
    addImage = JavaMethod(
        f"(Landroid/graphics/Bitmap;)"
        f"L{package_path}/type/Content$Builder;"
    )
    addFileData = JavaMethod(
        f"(Ljava/lang/String;Ljava/lang/String;)"
        f"L{package_path}/type/Content$Builder;"
    )
    build = JavaMethod(f"()L{package_path}/type/Content;")
