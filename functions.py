def get_structure_schema(schema_data):
    db_id = schema_data.get("db_id")
    table_names_original = schema_data.get("table_names_original")
    table_names = schema_data.get("table_names")
    column_names_original = schema_data.get("column_names_original")
    column_names = schema_data.get("column_names")
    column_types = schema_data.get("column_types")
    
    structured_schema = {"db_id": db_id, "tables": {}}
    
    # To keep track of the column types processed
    count = 1

    # Iterate over each table
    for i, table_name in enumerate(table_names_original):
        # Extract columns for the current table
        tab_col_nm = [row[1] for row in column_names_original if row[0] == i]
        tab_col_al = [row[1] for row in column_names if row[0] == i]
        
        # Slice column types based on number of columns for this table
        tab_col_typ = column_types[count: count + len(tab_col_nm)]
        count += len(tab_col_nm)

        table_alias = table_names[i]
        columns = []

        # Collect each column's details (original name, alias, and type)
        for col_info in zip(tab_col_nm, tab_col_al, tab_col_typ):
            original_col_info, alias_col_info, col_type = col_info
            columns.append({
                "original_name": original_col_info,
                "alias_name": alias_col_info,
                "type": col_type
            })

        # Store the columns for this table in the structured schema
        structured_schema["tables"][table_name] = {"columns": columns}

    return structured_schema
