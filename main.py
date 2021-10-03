from website import create_ssis

ssis = create_ssis()

if __name__ == '__main__':
    ssis.run(debug = True)