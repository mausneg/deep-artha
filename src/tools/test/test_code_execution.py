from dotenv import load_dotenv

from src.tools import upload_file, run_python_code

load_dotenv()

def test_upload_file():
    file_name = "apple_2024.xlsx"
    result = upload_file.invoke({"local_file_name": file_name})
    
    assert file_name in result
    
def test_run_python_code():
    code = """
    print("test")
    """
    
    result = run_python_code.invoke({"code": code})
    
    assert "test" in result