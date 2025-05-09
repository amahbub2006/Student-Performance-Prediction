import pandas as pd
import os
from studentml.logging.logger import logger
from studentml.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform(self):
        logger.info("Reading raw dataset...")
        df = pd.read_csv(self.config.source_path)

        # Use G2 as current grade
        df["current_grade"] = df["G2"]
        df = df[["current_grade", "studytime", "failures", "absences", "G3"]]

        rows = []

        for _, row in df.iterrows():
            current = int(row["current_grade"])
            final = int(row["G3"])

            for desired in range(current + 1, 21):
                jump = desired - current

                # Realistic success only for small jumps
                if jump <= 2 and final >= desired:
                    success = 1
                else:
                    success = 0

                rows.append({
                    "current_grade": current,
                    "desired_grade": desired,
                    "studytime": int(row["studytime"]),
                    "failures": int(row["failures"]),
                    "absences": int(row["absences"]),
                    "success": success
                })

        transformed_df = pd.DataFrame(rows)
        os.makedirs(os.path.dirname(
            self.config.transformed_data_path), exist_ok=True)
        transformed_df.to_csv(self.config.transformed_data_path, index=False)
        logger.info("✅ Data transformation completed and saved.")
        return transformed_df
