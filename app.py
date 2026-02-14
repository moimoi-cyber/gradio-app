# file: app.py
import gradio as gr
import subprocess

# ---- ダミーの「見つかりやすい秘密」：本物ではありません（テスト用） ----
#DUMMY_AWS_ACCESS_KEY = "AKIA1234567890EXAMPLE"
#DUMMY_AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
#DUMMY_GITHUB_TOKEN   = "ghp_1234567890abcdefghijklmnopqrstuvwxYZ"

def greet(name, intensity):
    # ---- 危険な例（SASTの典型）：ユーザー入力をシェルに直渡し。実運用では絶対NG ----
#    subprocess.run(f"echo {name}", shell=True)
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

if __name__ == "__main__":
    demo.launch()