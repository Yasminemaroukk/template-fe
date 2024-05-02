import os

def extract_secret_vars():
    branch = os.getenv("GITHUB_REF")
    print("Branch:", branch)  # Add this line for debug
    if branch:
        prefix = "DEV_" if branch == "refs/heads/dev" else "PROD_"
        print("Prefix:", prefix)  # Add this line for debug
        path_var = os.getenv(prefix + "PATH")
        print("Path Variable:", path_var)  # Add this line for debug
        if path_var:
            with open(".env", "w") as env_file:
                env_file.write(f"PATH={path_var}")
        else:
            raise ValueError(f"{prefix}PATH not found in secrets.")
    else:
        raise ValueError("GITHUB_REF environment variable not set.")

if __name__ == "__main__":
    extract_secret_vars()
