import os

def extract_secret_vars():
    branch = os.getenv("GITHUB_REF")
    if branch:
        if branch == "refs/heads/dev":
            prefix = "DEV_"
        elif branch == "refs/heads/prod":
            prefix = "PROD_"
        else:
            raise ValueError("Unsupported branch for deployment.")
        
        path_var = os.getenv(prefix + "PATH")
        if path_var:
            with open(".env", "w") as env_file:
                env_file.write(f"{prefix[:-1]}={path_var}")  # Write variable name without prefix to .env
        else:
            raise ValueError(f"{prefix}PATH not found in secrets.")
    else:
        raise ValueError("GITHUB_REF environment variable not set.")

if __name__ == "__main__":
    extract_secret_vars()
