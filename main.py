def main():
    deps = ["matplotlib", "networkx", "numpy", "pandas", "requests"]
    ok = True
    for dep in deps:
        try:
            __import__(dep)
            print(f"  [OK] {dep}")
        except ImportError:
            print(f"  [MISSING] {dep}")
            ok = False

    if ok:
        print("\nEnvironment OK")
    else:
        print("\nFaltam dependencias. Rode: uv sync")


if __name__ == "__main__":
    main()
