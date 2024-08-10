from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
)
from sjgeminifvai import package_path

__all__ = ("GenerateContentResponse", )


class GenerateContentResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/GenerateContentResponse"
    __javaconstructor__ = (
        f"(Ljava/util/List;"
        f"L{package_path}i/type/PromptFeedback;"
        f"L{package_path}/type/UsageMetadata;)V",
    )
    getCandidates = JavaMethod("()Ljava/util/List;")
    getPromptFeedback = JavaMethod(f"()L{package_path}/type/PromptFeedback;")
    getUsageMetadata = JavaMethod(f"()L{package_path}/type/UsageMetadata;")
    getText = JavaMethod("()Ljava/lang/String;")
    getFunctionCalls = JavaMethod("()Ljava/util/List;")
    getFunctionResponse = JavaMethod(f"()L{package_path}/type/FunctionResponsePart;")
