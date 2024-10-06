from openai_client import client
from file_process import correct_typos
from utils import write_file, processed_dir

file_name = "苏睿熹.txt"
correct_text = correct_typos(client,file_name)
write_file(processed_dir.joinpath(file_name), correct_text)
