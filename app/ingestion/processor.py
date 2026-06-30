from unstructured.documents.elements import Table


def process_elements(elements):
    """
    Separate parsed elements into
    text, tables and images.
    """

    processed = {
        "texts": [],
        "tables": [],
        "images": []
    }

    for element in elements:

        category = element.category

        if category == "Image":
            processed["images"].append(element)

        elif isinstance(element, Table):
            processed["tables"].append(element)

        else:
            processed["texts"].append(element)

    return processed