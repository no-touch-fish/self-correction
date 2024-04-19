from ml_collections import config_dict

def get_config():
    config = config_dict.ConfigDict()

    # tokenizers
    config.tokenizer_paths=['']
    config.tokenizer_kwargs=[{"use_fast": False}]
    # model
    config.model_paths=['']
    config.model_kwargs=[{"low_cpu_mem_usage": True, "use_cache": False}]
    config.conversation_templates=['llama2']
    config.devices=['cuda:2']
    # data
    config.train_data = ''
    config.test_data = ''
    config.n_train_data = 1
    config.n_test_data = 0
    # parameter
    config.batch_size = 1
    return config
