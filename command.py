import click  
import ollama

@click.command()
@click.argument('s', nargs=-1, required=0)
@click.option("-t", type=click.File('rb'))
def hello(s,t):
    str = ''
    if t:
        str = t.read()
    else:
        for item in s:
            str = str + item + ' '


    click.echo(ollama.pull("qwen2:0.5b"))
    response = ollama.chat(model='qwen2:0.5b', messages=[
    {
        'role': 'user',
        'content': f'briefly summarize in very few sentences, {str}',
    },
    ])
    click.echo(response['message']['content'])




if __name__ == "__main__":
    hello()