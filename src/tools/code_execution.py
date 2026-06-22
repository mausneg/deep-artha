from langchain.tools import tool
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv
import time
import base64
import os

load_dotenv()

@tool
def upload_file(local_file_name: str, timeout: int=300):
    """Upload a data file to the E2B Sandbox for analysis

    Args:
        local_file_name (str): Local path the file
        timeout (int): Time in seconds after which the code execution will be forcefully stopped. Default is 300 seconds.

    Returns:
        str : Success message with the sandbox path and dataset_info
    """
    
    sbx = Sandbox.create(timeout=timeout)
    
    local_file_name = local_file_name.lstrip('/').lstrip('\\')
    local_file_path = f"./data/{local_file_name}"

    if not os.path.exists(local_file_path):
        return f"Error: file not found at {local_file_path}"
    
    with open(local_file_path, "rb") as f:
        sandbox_file = sbx.files.write(f"data/{local_file_name}", f)
    
    sbx.kill()

    return f"File uploaded successfully!\nSandbox path: {sandbox_file.path}"


@tool
def run_python_code(code: str, timeout: int=300)-> str:
    """Execute python code in E2B sandbox

    Args:
        code (str): Valid executable Python code. Do not pass anything else other than python code.
        timeout (int): Time in seconds after which the code execution will be forcefully stopped. Default is 300 seconds.
                                
    Returns:
        str: Execution Result
    """
    
    sbx = Sandbox.create(timeout=timeout)
    execution = sbx.run_code(code)
    
    if execution.error:
        return f"Error: {execution.error.name}\nValue: {execution.error.value}"
        
    os.makedirs('images', exist_ok=True)

    output = []
    timestamp = int(time.time())

    output.append(str(execution))

    for idx, result in enumerate(execution.results):
        if result.png:
            filename = f'images/{timestamp}_chart_{idx}.png'
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(result.png))
            
            output.append(f"Chart saved to {filename}")

    sbx.kill()
    return "\n".join(output) if output else "Code executed but no output was returned"
    