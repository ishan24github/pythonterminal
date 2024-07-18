import click  
import ollama

@click.command()
@click.argument('usr_str', nargs=-1, required=0)
@click.option("-t", type=click.File('rb'))
def summary(usr_str,t):
    str = ''
    if t:
        str = t.read()
    else:
        for item in usr_str:
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
    summary()