import pandas as pd


class DataApp:
    def __init__(self):
        df_age_structures = pd.read_csv(
            "data_folder/age_structures.csv", skiprows=2, encoding="latin-1"
        )
        df_apartments = pd.read_csv(
            "data_folder/apartments.csv", skiprows=2, encoding="latin-1"
        )
        df_vehicles = pd.read_csv(
            "data_folder/vehicles.csv", skiprows=2, encoding="latin-1"
        )

        df_age_structures = df_age_structures.rename(
            columns={"2022": "values", "byggï¿½r": "year"}
        )
        df_apartments = df_apartments.rename(columns={"2022": "values"})
        df_vehicles = df_vehicles.rename(columns={"2022": "values"})

        # concatenate the dataframes with a new column type
        df_age_structures["type"] = "age_structure"
        df_apartments["type"] = "apartments"
        df_vehicles["type"] = "vehicles"
        self.df = pd.concat([df_age_structures, df_apartments, df_vehicles])
        self.df.reset_index(inplace=True)

    def _format_get(self, deso: str) -> pd.DataFrame:
        df = self.df[self.df["region"] == deso].iloc[:, 2:]
        print(df)
        return df

    def get(self, deso: str) -> str:
        try:
            out: str = self._format_get(deso).to_json()
        except KeyError:
            out: str = "No data found for this deso"
        return out


if __name__ == "__main__":
    app = DataApp()
    print(app.get("0114A0010"))
