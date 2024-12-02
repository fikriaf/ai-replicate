import os, replicate

# Set the environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_9fKjlnksX1LAgcXpWj624FlGkS5kmCd47Yjnc"

def respon(you):
    for event in replicate.run(
        "meta/meta-llama-3-70b-instruct",
        input={
            "prompt": you,
            "system_prompt": "Kamu adalah Aitwo, kamu seperti manusia pada umumnya, bisa berkomunikasi natural dan tidak kaku, serta menjawab se efektif mungkin"
        }
    ):
        print(str(event), end="")
