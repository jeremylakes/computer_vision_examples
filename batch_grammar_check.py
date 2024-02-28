import re
from tqdm.auto import tqdm
#@title define functions
#@markdown - this defines the `split_text` and `correct_text` functions
#@markdown - **NOTE:** you may need to adjust the regex in `split_text` depending on your source text

def split_text(text: str) -> list:
    """
    Split a string of text into a list of sentence batches.

    Parameters:
    text (str): The text to be split into sentence batches.

    Returns:
    list: A list of sentence batches. Each sentence batch is a list of sentences.
    """
    # Split the text into sentences using regex
    sentences = re.split(r"(?<=[^A-Z].[.?]) +(?=[A-Z])", text)

    # Initialize a list to store the sentence batches
    sentence_batches = []

    # Initialize a temporary list to store the current batch of sentences
    temp_batch = []

    # Iterate through the sentences
    for sentence in sentences:
        # Add the sentence to the temporary batch
        temp_batch.append(sentence)

        # If the length of the temporary batch is between 2 and 3 sentences, or if it is the last batch, add it to the list of sentence batches
        if len(temp_batch) >= 2 and len(temp_batch) <= 3 or sentence == sentences[-1]:
            sentence_batches.append(temp_batch)
            temp_batch = []

    return sentence_batches


def correct_text(text: str, checker, corrector, separator: str = " ") -> str:
    """
    Correct the grammar in a string of text using a text-classification and text-generation pipeline.

    Parameters:
    text (str): The text to be corrected.
    checker (transformers.pipeline.Pipeline): The text-classification pipeline to use for checking the grammar quality of the text.
    corrector (transformers.pipeline.Pipeline): The text-generation pipeline to use for correcting the text.
    separator (str, optional): The separator to use when joining the corrected text into a single string. Default is a space character.

    Returns:
    str: The corrected text.
    """
    # Split the text into sentence batches
    sentence_batches = split_text(text)

    # Initialize a list to store the corrected text
    corrected_text = []

    # Iterate through the sentence batches
    for batch in tqdm(
        sentence_batches, total=len(sentence_batches), desc="correcting text.."
    ):
        # Join the sentences in the batch into a single string
        raw_text = " ".join(batch)

        # Check the grammar quality of the text using the text-classification pipeline
        results = checker(raw_text)

        # Only correct the text if the results of the text-classification are not LABEL_1 or are LABEL_1 with a score below 0.9
        if results[0]["label"] != "LABEL_1" or (
            results[0]["label"] == "LABEL_1" and results[0]["score"] < 0.9
        ):
            # Correct the text using the text-generation pipeline
            corrected_batch = corrector(raw_text)
            corrected_text.append(corrected_batch[0]["generated_text"])
        else:
            corrected_text.append(raw_text)

    # Join the corrected text into a single string
    corrected_text = separator.join(corrected_text)

    return corrected_text
    
    
#@title enter text to correct
raw_text = "the toweris 324 met (1,063 ft) tall, about height as .An 81-storey building, and biggest longest structure paris. Is square, measuring 125 metres (410 ft) on each side. During its constructiothe eiffel tower surpassed the washington monument to become the tallest man-made structure in the world, a title it held for 41 yearsuntilthe chryslerbuilding in new york city was finished in 1930. It was the first structure to goat a height of 300 metres. Due 2 the addition ofa brdcasting aerial at the t0pp of the twr in 1957, it now taller than  chrysler building 5.2 metres (17 ft). Exxxcluding transmitters,  eiffel tower is  2ndd tallest ree-standing structure in france after millau viaduct." #@param {type:"string"}

import pprint as pp
pp.pprint(raw_text)

# Initialize the text-classification pipeline
from transformers import pipeline
checker = pipeline("text-classification", "textattack/roberta-base-CoLA")

# Initialize the text-generation pipeline
from transformers import pipeline
corrector = pipeline(
        "text2text-generation",
        "pszemraj/flan-t5-large-grammar-synthesis",
    )

# Correct the text using the correct_text function
corrected_text = correct_text(raw_text, checker, corrector)
pp.pprint(corrected_text)



