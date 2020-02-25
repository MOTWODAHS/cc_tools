import cc_dat_utils
import cc_classes
import json

def make_cc_level_pack_from_json(json_data):
    pack = cc_classes.CCLevelPack()

    # read data from each level
    for level_data in json_data:
        level = cc_classes.CCLevel()
        level.level_number = level_data['level_number']
        level.time = level_data['time']
        level.num_chips = level_data['num_chips']
        level.upper_layer = level_data['upper_layer']
        level.lower_layer = level_data['lower_layer']

        level.optional_fields = []

        for field_data in level_data['optional_fields']:
            # Handle title field
            if field_data['field_name'] == "title":
                title_field = cc_classes.CCMapTitleField(field_data['value'])
                level.optional_fields.append(title_field)
                continue
            # Handle hint field
            elif field_data['field_name'] == "hint":
                hint_field = cc_classes.CCMapHintField(field_data['value'])
                level.optional_fields.append(hint_field)
                continue
            # Handle encoded password field
            elif field_data['field_name'] == "encoded_password":
                encoded_passoword_field = cc_classes.CCEncodedPasswordField(field_data['value'])
                level.optional_fields.append(encoded_passoword_field)
                continue
            # Handle monster field
            elif field_data['field_name'] == "monster":
                monster_coords_list = []
                for coords in field_data['value']:
                    current_coord = cc_classes.CCCoordinate(coords[0], coords[1])
                    monster_coords_list.append(current_coord)
                monster_field = cc_classes.CCMonsterMovementField(monster_coords_list)
                level.optional_fields.append(monster_field)
            # Handle trap field
            elif field_data['field_name'] == "trap":
                trap_coords_list = []
                for coords in field_data['value']:
                    trap_control = cc_classes.CCTrapControl(coords[0], coords[1], coords[2], coords[3])
                    trap_coords_list.append(trap_control)
                trap_field = cc_classes.CCTrapControlsField(trap_coords_list)
                level.optional_fields.append(trap_field)
            # Handle cloning_machine field
            elif field_data['field_name'] == "cloning_machine":
                cloning_coords_list = []
                for coords in field_data['value']:
                    cloning_control = cc_classes.CCCloningMachineControl(coords[0], coords[1], coords[2], coords[3])
                    cloning_coords_list.append(cloning_control)
                cloning_field = cc_classes.CCCloningMachineControlsField(cloning_coords_list)
                level.optional_fields.append(cloning_field)
        # Add level to level pack
        pack.add_level(level)
    return pack


#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

input_json_file = "data/xuhaod_cc1.json"
with open(input_json_file) as f:
    data = json.load(f)

level_pack = make_cc_level_pack_from_json(data)

out_dat_file = "data/xuhaod_cc1.dat"

cc_dat_utils.write_cc_level_pack_to_dat(level_pack, out_dat_file)

# input_dat_file = "data/xuhaod_cc1.dat"
# data = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)
# print(data)