
import os
import pandas as pd

from data_cleaning import load_data, cleaning
from data_Analysis import Analysis_data


def main():

    # Step 1: Create reports folder
    os.makedirs("reports", exist_ok=True)

    print("=" * 50)
    print("       E-COMMERCE DATA ANALYSIS")
    print("=" * 50)

    try:
        # Step 2: Load datasets
        print("\n[1] Loading datasets...")

        cu, ore, prod = load_data()

        print("Customers Dataset:", cu.shape)
        print("Orders Dataset:", ore.shape)
        print("Products Dataset:", prod.shape)

        print("\nDatasets loaded successfully!")

        # Step 3: Clean datasets
        print("\n[2] Cleaning datasets...")

        cu, ore, prod = cleaning(cu, ore, prod)

        print("Data cleaning completed successfully!")

        # Step 4: Perform analysis
        print("\n[3] Performing data analysis...")

        summary = Analysis_data(cu, ore, prod)

        # Step 5: Generate final report
        print("\n[4] Generating final report...")

        report_lines = [
            "E-COMMERCE DATA ANALYSIS REPORT",
            "=" * 50,
            ""
        ]

        for question, answer in summary.items():

            report_lines.append(question)
            report_lines.append("-" * 50)

            print(f"\n{question}")

            if isinstance(answer, pd.DataFrame):

                if answer.empty:
                    result = "No records found."
                else:
                    result = answer.to_string(index=False)

                print(result)
                report_lines.append(result)

            else:
                result = str(answer)

                print(result)
                report_lines.append(result)

            report_lines.append("")

        # Step 6: Save TXT report
        txt_path = os.path.join(
            "reports",
            "final_report.txt"
        )

        with open(txt_path, "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))

        # Step 7: Save CSV report
        csv_data = []

        for question, answer in summary.items():

            if isinstance(answer, pd.DataFrame):
                result = answer.to_json(
                    orient="records",
                    force_ascii=False
                )
            else:
                result = str(answer)

            csv_data.append({
                "Business_Question": question,
                "Analysis_Result": result
            })

        report_df = pd.DataFrame(csv_data)

        csv_path = os.path.join(
            "reports",
            "final_report.csv"
        )

        report_df.to_csv(
            csv_path,
            index=False,
            encoding="utf-8-sig"
        )

        # Step 8: Display completion message
        print("\n" + "=" * 50)
        print("REPORT GENERATED SUCCESSFULLY!")
        print("=" * 50)

        print(f"\nTXT Report: {txt_path}")
        print(f"CSV Report: {csv_path}")

        print("\nProject completed successfully!")

    except FileNotFoundError as error:
        print("\nERROR: Dataset file not found.")
        print("Check your Data folder and CSV filenames.")
        print("Details:", error)

    except KeyError as error:
        print("\nERROR: Required column not found in dataset.")
        print("Check your CSV column names.")
        print("Details:", error)

    except Exception as error:
        print("\nERROR: Something went wrong.")
        print("Details:", error)


if __name__ == "__main__":
    main()

