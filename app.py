import gradio as gr
import subprocess
import sys

def greet(name, intensity):
    # コマンドインジェクションの例：
    subprocess.run(f"echo {name}", shell=True)
    return "Hello, " + name + "!" * int(intensity)

def main():
    # Gradio画面のテキストボックスに入れた内容が、そのまま greet() の name に入る。
    demo = gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
        api_name="predict"
    )

    # 引数が1つ以上あれば、その最初の引数をnameとしてコマンドに流し込む。
    if len(sys.argv) > 1:
        name = sys.argv[1]
        subprocess.run(f"echo {name}", shell=True)

    demo.launch()

if __name__ == "__main__":
    main()