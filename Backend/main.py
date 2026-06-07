from pipeline.outreach import run_pipeline


def main():
    print("\n" + "=" * 60)
    print("AUTOMATED OUTREACH PIPELINE")
    print("=" * 60)

    domain = input(
        "\nEnter company domain (e.g. brex.com): "
    ).strip().lower()

    if not domain:
        print("Domain is required.")
        return

    try:
        run_pipeline(domain)

    except KeyboardInterrupt:
        print("\nPipeline cancelled by user.")

    except Exception as e:
        print(f"\nPipeline failed: {e}")


if __name__ == "__main__":
    main()