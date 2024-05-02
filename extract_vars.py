import os

def extract_secret_vars():
    print(os.environ)  # Print all environment variables for debugging
    branch = os.getenv("GITHUB_REF")
    print("Branch:", branch)  # Print the branch for debugging
    if branch:
        if branch == "refs/heads/dev":
            prefix = "DEV_"
        elif branch == "refs/heads/prod":
            prefix = "PROD_"
        else:
            raise ValueError("Unsupported branch for deployment.")
        
        path_var = os.getenv(prefix + "PATH")
        print(prefix + "PATH:", path_var)  # Print the secret variable for debugging
        if path_var:
            with open(".env", "w") as env_file:
                env_file.write(f"{prefix[:-1]}={path_var}")  # Write variable name without prefix to .env
        else:
            raise ValueError(f"{prefix}PATH not found in secrets.")
    else:
        raise ValueError("GITHUB_REF environment variable not set.")

if __name__ == "__main__":
    extract_secret_vars()
