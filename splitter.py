import os
from PyPDF2 import PdfReader, PdfWriter

def get_files():
    files = [file for file in os.listdir(path="assets/") if file.endswith('.pdf')]
    dir = enumerate(files, start=1)
    print("Choose file to split.\n")
    data = dict(dir)
    print('\n'.join(f"{i}. {file}" for i, file in data.items()))
    
    return data
    

def split_pdf(input_file, chunk_size, output_dir="."):
    """
    Splits a PDF into smaller PDFs with given chunk size.

    Args:
        input_file (str): Path to input PDF file.
        chunk_size (int): Number of pages per split file.
        output_dir (str): Directory to save the output files.
    """
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    reader = PdfReader(f"assets/{input_file}")
    total_pages = len(reader.pages)

    for i in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        for j in range(i, min(i + chunk_size, total_pages)):
            writer.add_page(reader.pages[j])

        output_file = os.path.join(output_dir, f"{i//chunk_size + 1}.pdf")
        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"Saved: {output_file}")


def main():
    while True:
        data = get_files()
        try:
            choice = int(input("\nType number of option: "))
            chunk_size = int(input("Type chunk size: "))
            input_pdf = data[choice]
            split_pdf(input_pdf, chunk_size)
        except Exception as e:
            os.system('cls')
            print("Sorry! an error occured:", e, '\n')
        else:
            break


if __name__ == "__main__":
    main()
