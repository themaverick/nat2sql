def get_structure_schema(schema_data):
    db_id = schema_data.get("db_id")
    table_names_original = schema_data.get("table_names_original")
    table_names = schema_data.get("table_names")
    column_names_original = schema_data.get("column_names_original")
    column_names = schema_data.get("column_names")
    column_types = schema_data.get("column_types")
    
    structured_schema = {"db_id": db_id, "tables": {}}
    
    # Iterate over each table
    for i, table_name in enumerate(table_names_original):
        table_alias = table_names[i]
        columns = []
        
        # For each column in this table, match original names with alias and types
        for col_info in zip(column_names_original, column_names, column_types):
            original_col_info, alias_col_info, col_type = col_info
            if original_col_info[0] == i:  # Check if this column belongs to the current table
                columns.append({
                    "original_name": original_col_info[1],
                    "alias_name": alias_col_info[1],
                    "type": col_type
                })
        
        # Store the columns for each table
        structured_schema["tables"][table_alias] = {"columns": columns}
    
    return structured_schema