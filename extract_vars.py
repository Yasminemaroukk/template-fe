import os

def extract_secret_vars():
    branch = os.getenv("GITHUB_REF")
    if branch:
        prefix = "DEV_" if branch == "refs/heads/dev" else "PROD_"
        path_var = os.getsecret(prefix + "PATH")
        if path_var:
            with open(".env", "w") as env_file:
                env_file.write(f"PATH={path_var}")
        else:
            raise ValueError(f"{prefix}PATH not found in secrets.")
    else:
        raise ValueError("GITHUB_REF environment variable not set.")

if __name__ == "__main__":
    extract_secret_vars()
