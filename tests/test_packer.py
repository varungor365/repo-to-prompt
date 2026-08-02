import os
import tempfile

from repo2prompt.packer import pack_repo


def test_pack_repo():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files
        with open(os.path.join(temp_dir, "main.py"), "w") as f:
            f.write("print('hello')")
            
        with open(os.path.join(temp_dir, ".gitignore"), "w") as f:
            f.write("secret.txt\n")
            
        with open(os.path.join(temp_dir, "secret.txt"), "w") as f:
            f.write("api_key=123")
            
        # Create a nested ignored dir
        os.makedirs(os.path.join(temp_dir, "node_modules"))
        with open(os.path.join(temp_dir, "node_modules", "test.js"), "w") as f:
            f.write("console.log('ignored')")
            
        prompt = pack_repo(temp_dir)
        
        assert "main.py" in prompt
        assert "print('hello')" in prompt
        
        # Ignored files shouldn't be there
        assert "secret.txt" not in prompt
        assert "api_key=123" not in prompt
        
        # Default ignores shouldn't be there
        assert "node_modules/test.js" not in prompt
        assert "console.log('ignored')" not in prompt
