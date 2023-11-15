# config file
import json


class Config:
    """Config class for GPT Researcher."""

    def __init__(self, config_file: str = None):
        """Initialize the config class."""
        self.config_file = config_file
        self.retriever = "tavily"
        self.llm_provider = "ChatOpenAI"
        # gpt-3.5-turbo-16k to gpt-4-1106-preview
        self.fast_llm_model = " gpt-3.5-turbo-16k"
        self.smart_llm_model = "gpt-4-1106-preview"
        # 2000 to 4000
        self.fast_token_limit = 4000
        # 4000
        self.smart_token_limit = 4000
        # 8192 to 16000
        self.browse_chunk_max_length = 8000
        # 700 to 1400
        self.summary_token_limit = 1400
        self.temperature = 0.6
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
                          " Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        self.memory_backend = "local"
        # 1000 to 1500
        self.total_words = 1500
        self.report_format = "apa"
        self.max_iterations = 1

        self.load_config_file()

    def load_config_file(self) -> None:
        """Load the config file."""
        if self.config_file is None:
            return None
        with open(self.config_file, "r") as f:
            config = json.load(f)
        for key, value in config.items():
            self.__dict__[key] = value

