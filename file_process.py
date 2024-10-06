from utils import files_dir

def correct_typos(client, filename):
    file_path = files_dir.joinpath(filename)
    text = file_path.read_text(encoding='utf-8')
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user",
             "content": "根据上下文修改文章的错别字，不需要大量改动，使得语句通顺即可，并给出修改后的文章。\n" + text 
            }
        ]
    )
    return response.choices[0].message.content