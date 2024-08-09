from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaField,
    JavaMethod
)
from sjgeminifvai import package_path

__all__ = ("GenerationConfigBuilder", )


class GenerationConfigBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = f"{package_path}/type/GenerationConfig$Builder"

    temperature = JavaField("Ljava/lang/Float;")
    topK = JavaField("Ljava/lang/Integer;")
    topP = JavaField("Ljava/lang/Float;")
    candidateCount = JavaField("Ljava/lang/Integer;")
    maxOutputTokens = JavaField("Ljava/lang/Integer;")
    stopSequences = JavaField("Ljava/util/List;")
    responseMimeType = JavaField("Ljava/lang/String;")
    responseSchema = JavaField(f"L{package_path}/type/Schema;")
    build = JavaMethod(f"()L{package_path}/type/GenerationConfig;")
