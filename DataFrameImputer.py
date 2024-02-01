
class DataframeImputer:

    def impute_missing_values(self, df):
        
        for col in df.columns:
            if df[col].isnull().any():
                mode_value = df[col].mode()[0] 
                df[col].fillna(mode_value, inplace=True)

        return df

