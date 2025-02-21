
''' The highly correlated features for each target variable in each
     production line by feature selection '''

def get_feature(line, type_, target):

    if line == 'A2' and type_ == 'N':
        if target == 'Electricity':
            features = ['Host speed', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 7',
                        'Oven speed 8', 'Oven temperature 1', 'Oven temperature 7', 'Oven temperature 8', 'Oven temperature setting 2',
                        'Oven temperature setting 3', 'Oven temperature setting 8', 'Exhaust speed 1', 'Exhaust speed 2', 'Bwin 4']

        elif target == 'Moisture':
            features = ['Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7',
                        'Oven speed 8', 'Oven temperature 4', 'Oven temperature setting 8', 'Exhaust speed 1', 'Exhaust speed 2']

        elif target == 'Width':
            features = ['Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7',
                        'Oven speed 8', 'Oven temperature 4', 'Exhaust speed 1', 'Exhaust speed 2', 'Bwin 1']

        elif target == 'Weight':
            features = ['F_UNIT_P', 'Host speed', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6',
                        'Oven speed 7', 'Oven speed 8', 'Exhaust speed 1', 'Exhaust speed 2', 'Bwin 4']

    elif line == 'A2' and type_ == 'P':
        if target == 'Electricity':
            features = ['Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 7', 'Oven temperature 5', 'Oven temperature 6',
                        'Oven temperature setting 1', 'Oven temperature setting 7', 'Oven temperature setting 8', 'Humidity in the venue', 'Bwin 1']

        elif target == 'Moisture':
            features = ['Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 1',
                        'Oven temperature 4', 'Oven temperature setting 1', 'Oven temperature setting 5', 'Oven temperature setting 7', 'Bwin 4']

        elif target == 'Width':
            features = ['F_UNIT_P', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven temperature 1',
                        'Oven temperature 4', 'Oven temperature 8', 'Oven temperature setting 6', 'Bwin 1', 'Bwin 3']


        elif target == 'Weight':
            features = ['F_UNIT_P', 'Sizing machine speed', 'Feeding speed at the entrance', 'Entrance lower wheel speed',
                        'Exit lower wheel speed', 'Oven speed 1', 'Oven speed 4', 'Oven speed 5', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 1',
                        'Oven temperature 3', 'Oven temperature 4', 'Oven temperature 5', 'Oven temperature 8', 'Temperature valve opening 1', 'Temperature valve opening 2',
                        'Temperature valve opening 3', 'Temperature valve opening 4', 'Temperature valve opening 6', 'Temperature valve opening 8',
                        'Oven temperature setting 2', 'Oven temperature setting 4', 'Oven temperature setting 6', 'Oven temperature setting 7',
                        'Heat transfer oil supply temperature', 'Thermal oil cumulative flow', 'Exhaust speed 1', 'Exhaust speed 2',
                        'Humidity in the venue', 'Bwin 1', 'Bwin 2']


    elif line == 'A1' and type_ == 'N':
        if target == 'Electricity':
            features = ['Cold air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8',
                        'Oven temperature 1', 'Oven temperature 2', 'Oven temperature 6', 'Oven temperature 7', 'Oven temperature setting 2', 'Oven temperature setting 4',
                        'Oven temperature setting 7', 'Exhaust speed 1', 'Exhaust speed 2', 'Thermal_Temper_W', 'Thermal_Temper_E', 'Thermal_Temper_SE']

        elif target == 'Moisture':
            features = ['Cold air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8',
                        'Oven temperature 2', 'Oven temperature 4', 'Oven temperature 7', 'Oven temperature setting 2', 'Exhaust speed 1', 'Exhaust speed 2']

        elif target == 'Width':
            features = ['Cold air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8',
                        'Oven temperature setting 6', 'Exhaust speed 1', 'Exhaust speed 2', 'Thermal_Temper_NE', 'Thermal_Temper_SW', 'Thermal_Temper_S']

        elif target == 'Weight':
            features = ['F_COLOR_SEQ', 'F_UNIT_P', 'Cold air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6',
                        'Oven speed 7', 'Oven speed 8', 'Oven temperature 1', 'Oven temperature 3', 'Oven temperature 7', 'Oven temperature 8', 'Oven temperature setting 6',
                        'Oven temperature setting 7', 'Exhaust speed 1', 'Exhaust speed 2', 'Thermal_Temper_NW', 'Thermal_Temper_NE', 'Thermal_Temper_W', 'Thermal_Temper_E',
                        'Thermal_Temper_S', 'Thermal_Temper_avg', 'Thermal_Spot1_Temper_max', 'Thermal_Full_min', 'Thermal_Full_max']

    elif line == 'A1' and type_ == 'P':
        if target == 'Electricity':
            features = ['Cool air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 2',
                        'Oven temperature 6', 'Oven temperature 7', 'Oven temperature 8', 'Oven temperature setting 3', 'Oven temperature setting 7', 'Exhaust speed 1', 'Exhaust speed 2',
                        'Thermal_Temper_NW', 'Thermal_Temper_E', 'Thermal_Temper_SW', 'Thermal_Temper_SE', 'Thermal_Full_min', 'Thermal_Full_avg']

        elif target == 'Moisture':
            features = ['Cool air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 1',
                        'Oven temperature 2', 'Oven temperature 3', 'Oven temperature 4', 'Oven temperature 5', 'Oven temperature 6', 'Oven temperature 7', 'Oven temperature 8', 'Oven temperature setting 1',
                        'Oven temperature setting 2', 'Oven temperature setting 3', 'Oven temperature setting 4', 'Oven temperature setting 5', 'Oven temperature setting 6', 'Oven temperature setting 7',
                        'Oven temperature setting 8', 'Exhaust speed 1', 'Exhaust speed 2', 'Thermal_Temper_NW', 'Thermal_Temper_NE', 'Thermal_Temper_W', 'Thermal_Temper_E', 'Thermal_Temper_SE', 'Thermal_Temper_avg',
                        'Thermal_Spot1_Temper_avg', 'Thermal_Spot1_Temper_max', 'Thermal_Full_avg', 'Thermal_Full_max']


        elif target == 'Width':
            features = ['Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Exhaust speed 1', 'Exhaust speed 2']


        elif target == 'Weight':
            features = ['Cool air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 1', 'Oven temperature 3',
                        'Oven temperature 4', 'Oven temperature 5', 'Oven temperature 6', 'Oven temperature 7', 'Oven temperature 8', 'Oven temperature setting 2', 'Oven temperature setting 3', 'Oven temperature setting 4',
                        'Oven temperature setting 5', 'Oven temperature setting 7', 'Oven temperature setting 8', 'Exhaust speed 1', 'Exhaust speed 2', 'Thermal_Temper_N', 'Thermal_Temper_NE', 'Thermal_Temper_W', 'Thermal_Temper_C',
                        'Thermal_Temper_E', 'Thermal_Temper_SW', 'Thermal_Temper_S', 'Thermal_Temper_avg', 'Thermal_Spot1_Temper_min', 'Thermal_Spot1_Temper_max', 'Thermal_Full_min', 'Thermal_Full_avg', 'Thermal_Full_max']


    elif line == 'BB' and type_ == '':
        if target == 'Electricity':
            features = ['Cool air speed 2', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 2', 'Oven temperature 6',
                        'Oven temperature setting 4', 'Oven temperature setting 7', 'Exhaust speed 1', 'Exhaust speed 2']


        elif target == 'Moisture':
            features = ['Shrink code', 'Finished cloth weight', 'Machine setting width', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4',
                        'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 4', 'Oven temperature setting 4', 'Oven temperature setting 8', 'Exhaust speed 2', 'Exhaust speed 3',
                        'Exhaust speed 4', 'Cool air speed 2', 'Bwin 3', 'Thermal_Temper_NE', 'Thermal_Temper_W', 'Thermal_Temper_avg']


        elif target == 'Width':
            features = ['Finished product width', 'Machine setting width', 'Oven speed 1', 'Oven speed 2', 'Oven speed 4', 'Oven speed 5', 'Oven speed 6', 'Exhaust speed 2',
                        'Exhaust speed 3', 'Exhaust speed 4']


        elif target == 'Weight':
            features = ['Shrink code', 'Zero drying width', 'Finished cloth weight', 'Machine setting width', 'Oven speed 1', 'Oven speed 2', 'Oven speed 3', 'Oven speed 4',
                        'Oven speed 5', 'Oven speed 6', 'Oven speed 7', 'Oven speed 8', 'Oven temperature 6', 'Oven temperature setting 5', 'Exhaust speed 1', 'Exhaust speed 2', 'Exhaust speed 3', 'Exhaust speed 4', 'Bwin 4',
                        'Thermal_Temper_SW', 'Thermal_Temper_avg']

    return features

