import purecl.common.const as cl

ERRORS = {
        cl.CL_SUCCESS: "CL_SUCCESS",
        cl.CL_DEVICE_NOT_FOUND: "CL_DEVICE_NOT_FOUND",
        cl.CL_DEVICE_NOT_AVAILABLE: "CL_DEVICE_NOT_AVAILABLE",
        cl.CL_COMPILER_NOT_AVAILABLE: "CL_COMPILER_NOT_AVAILABLE",
        cl.CL_MEM_OBJECT_ALLOCATION_FAILURE:
        "CL_MEM_OBJECT_ALLOCATION_FAILURE",
        cl.CL_OUT_OF_RESOURCES: "CL_OUT_OF_RESOURCES",
        cl.CL_OUT_OF_HOST_MEMORY: "CL_OUT_OF_HOST_MEMORY",
        cl.CL_PROFILING_INFO_NOT_AVAILABLE: "CL_PROFILING_INFO_NOT_AVAILABLE",
        cl.CL_MEM_COPY_OVERLAP: "CL_MEM_COPY_OVERLAP",
        cl.CL_IMAGE_FORMAT_MISMATCH: "CL_IMAGE_FORMAT_MISMATCH",
        cl.CL_IMAGE_FORMAT_NOT_SUPPORTED: "CL_IMAGE_FORMAT_NOT_SUPPORTED",
        cl.CL_BUILD_PROGRAM_FAILURE: "CL_BUILD_PROGRAM_FAILURE",
        cl.CL_MAP_FAILURE: "CL_MAP_FAILURE",
        cl.CL_MISALIGNED_SUB_BUFFER_OFFSET: "CL_MISALIGNED_SUB_BUFFER_OFFSET",
        cl.CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST:
        "CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST",
        cl.CL_COMPILE_PROGRAM_FAILURE: "CL_COMPILE_PROGRAM_FAILURE",
        cl.CL_LINKER_NOT_AVAILABLE: "CL_LINKER_NOT_AVAILABLE",
        cl.CL_LINK_PROGRAM_FAILURE: "CL_LINK_PROGRAM_FAILURE",
        cl.CL_DEVICE_PARTITION_FAILED: "CL_DEVICE_PARTITION_FAILED",
        cl.CL_KERNEL_ARG_INFO_NOT_AVAILABLE:
        "CL_KERNEL_ARG_INFO_NOT_AVAILABLE",

        cl.CL_INVALID_VALUE: "CL_INVALID_VALUE",
        cl.CL_INVALID_DEVICE_TYPE: "CL_INVALID_DEVICE_TYPE",
        cl.CL_INVALID_PLATFORM: "CL_INVALID_PLATFORM",
        cl.CL_INVALID_DEVICE: "CL_INVALID_DEVICE",
        cl.CL_INVALID_CONTEXT: "CL_INVALID_CONTEXT",
        cl.CL_INVALID_QUEUE_PROPERTIES: "CL_INVALID_QUEUE_PROPERTIES",
        cl.CL_INVALID_COMMAND_QUEUE: "CL_INVALID_COMMAND_QUEUE",
        cl.CL_INVALID_HOST_PTR: "CL_INVALID_HOST_PTR",
        cl.CL_INVALID_MEM_OBJECT: "CL_INVALID_MEM_OBJECT",
        cl.CL_INVALID_IMAGE_FORMAT_DESCRIPTOR:
        "CL_INVALID_IMAGE_FORMAT_DESCRIPTOR",
        cl.CL_INVALID_IMAGE_SIZE: "CL_INVALID_IMAGE_SIZE",
        cl.CL_INVALID_SAMPLER: "CL_INVALID_SAMPLER",
        cl.CL_INVALID_BINARY: "CL_INVALID_BINARY",
        cl.CL_INVALID_BUILD_OPTIONS: "CL_INVALID_BUILD_OPTIONS",
        cl.CL_INVALID_PROGRAM: "CL_INVALID_PROGRAM",
        cl.CL_INVALID_PROGRAM_EXECUTABLE: "CL_INVALID_PROGRAM_EXECUTABLE",
        cl.CL_INVALID_KERNEL_NAME: "CL_INVALID_KERNEL_NAME",
        cl.CL_INVALID_KERNEL_DEFINITION: "CL_INVALID_KERNEL_DEFINITION",
        cl.CL_INVALID_KERNEL: "CL_INVALID_KERNEL",
        cl.CL_INVALID_ARG_INDEX: "CL_INVALID_ARG_INDEX",
        cl.CL_INVALID_ARG_VALUE: "CL_INVALID_ARG_VALUE",
        cl.CL_INVALID_ARG_SIZE: "CL_INVALID_ARG_SIZE",
        cl.CL_INVALID_KERNEL_ARGS: "CL_INVALID_KERNEL_ARGS",
        cl.CL_INVALID_WORK_DIMENSION: "CL_INVALID_WORK_DIMENSION",
        cl.CL_INVALID_WORK_GROUP_SIZE: "CL_INVALID_WORK_GROUP_SIZE",
        cl.CL_INVALID_WORK_ITEM_SIZE: "CL_INVALID_WORK_ITEM_SIZE",
        cl.CL_INVALID_GLOBAL_OFFSET: "CL_INVALID_GLOBAL_OFFSET",
        cl.CL_INVALID_EVENT_WAIT_LIST: "CL_INVALID_EVENT_WAIT_LIST",
        cl.CL_INVALID_EVENT: "CL_INVALID_EVENT",
        cl.CL_INVALID_OPERATION: "CL_INVALID_OPERATION",
        cl.CL_INVALID_GL_OBJECT: "CL_INVALID_GL_OBJECT",
        cl.CL_INVALID_BUFFER_SIZE: "CL_INVALID_BUFFER_SIZE",
        cl.CL_INVALID_MIP_LEVEL: "CL_INVALID_MIP_LEVEL",
        cl.CL_INVALID_GLOBAL_WORK_SIZE: "CL_INVALID_GLOBAL_WORK_SIZE",
        cl.CL_INVALID_PROPERTY: "CL_INVALID_PROPERTY",
        cl.CL_INVALID_IMAGE_DESCRIPTOR: "CL_INVALID_IMAGE_DESCRIPTOR",
        cl.CL_INVALID_COMPILER_OPTIONS: "CL_INVALID_COMPILER_OPTIONS",
        cl.CL_INVALID_LINKER_OPTIONS: "CL_INVALID_LINKER_OPTIONS",
        cl.CL_INVALID_DEVICE_PARTITION_COUNT:
        "CL_INVALID_DEVICE_PARTITION_COUNT",
        cl.CL_INVALID_PIPE_SIZE: "CL_INVALID_PIPE_SIZE",
        cl.CL_INVALID_DEVICE_QUEUE: "CL_INVALID_DEVICE_QUEUE"
    }