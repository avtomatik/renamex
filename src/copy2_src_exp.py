import shutil
from pathlib import Path


def copy2_src_exp(FILE_NAMES, PATH_SRC, PATH_EXP):
    for file_name in FILE_NAMES:
        shutil.copy2(
            Path(PATH_SRC).joinpath(file_name),
            Path(PATH_EXP).joinpath(file_name)
        )


if __name__ == '__main__':
    PATH_SRC = '/media/green-machine/904F-3DB1/reports/latex'

    PATH_EXP = '/media/green-machine/KINGSTON'

    FILE_NAMES = (
        'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_en.tex',
        'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_ru.tex',
        'reference_en_samuelson_p_a_paul_douglas_s_measurement.tex',
        'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_en.pdf',
        'reference_en_douglas_p_h_cobb_douglas_production_function_once_again_ru.pdf',
        'reference_en_samuelson_p_a_paul_douglas_s_measurement.pdf',
    )

    copy2_src_exp(FILE_NAMES, PATH_SRC, PATH_EXP)
