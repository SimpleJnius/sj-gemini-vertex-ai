from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaStaticMethod,
    JavaMethod,
    JavaMultipleMethod
)
from sjgeminifvai import package_path

__all__ = ("GenerativeModelFutures", )


class GenerativeModelFutures(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/java/GenerativeModelFutures"

    generateContent = JavaMethod(
        f"([L{package_path}/type/Content;)"
        f"Lcom/google/common/util/concurrent/ListenableFuture;"
    )

    generateContentStream = JavaMethod(
        f"([L{package_path}/type/Content;)"
        f"Lorg/reactivestreams/Publisher;"
    )

    countTokens = JavaMethod(
        f"([L{package_path}/type/Content;)"
        f"Lcom/google/common/util/concurrent/ListenableFuture;"
    )

    startChat = JavaMultipleMethod([
        (
            f"()L{package_path}/java/ChatFutures;",
            False, False
        ),
        (
            f"(Ljava/util/List;)"
            f"L{package_path}/java/ChatFutures;",
            False, False
        )
    ])

    getGenerativeModel = JavaMethod(f"()L{package_path}/GenerativeModel;")

    locals()["from"] = JavaStaticMethod(
        f"(L{package_path}/GenerativeModel;)"
        f"L{package_path}/java/GenerativeModelFutures;"
    )
    from_ = locals()["from"]
