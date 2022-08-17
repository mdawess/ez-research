# Using CO:HERE for the text summarization
# Docs can be found here: https://docs.cohere.ai/generate-reference
# Project repo: https://github.com/cohere-ai

import cohere
import os
from typing import List, Tuple

API_KEY = os.environ.get("COHERE_API_KEY")
co = cohere.Client(API_KEY)


def create_summary(
    prompt: str,
    model: str,
    max_tokens: int,
    n_generations: int,
    temperature: float = 0.7,
    k: int = 0,
    p: float = 0.75,
) -> Tuple[List[str], List[float]]:
    """
    Create a summary for a given prompt using the CO:HERE API. Full credit to the summarization
    goes to CO:HERE.
    """
    prediction = co.generate(
        model=model,
        prompt=prompt,
        return_likelihoods="GENERATION",
        # stop_sequences=['"'],
        max_tokens=max_tokens,
        temperature=temperature,
        num_generations=n_generations,
        k=k,
        p=p,
    )

    gens = []
    likelihoods = []
    for gen in prediction.generations:
        gens.append(gen.text)

    sum_likelihood = 0
    for t in gen.token_likelihoods:
        sum_likelihood += t.likelihood
    # Get sum of likelihoods
    likelihoods.append(sum_likelihood)

    return gens, likelihoods


if __name__ == "__main__":
    # Sample from https://docs.cohere.ai/text-summarization-example/
    sample_prompt = """
        "The killer whale or orca (Orcinus orca) is a toothed whale
        belonging to the oceanic dolphin family, of which it is the largest member"
        In summary: "The killer whale or orca is the largest type of dolphin"

        "It is recognizable by its black-and-white patterned body"
        In summary:"Its body has a black and white pattern"

        "Killer whales have a diverse diet, although individual populations often specialize in particular types of prey"
        In summary:"
    """
    print(create_summary(sample_prompt, "small", 50, 5)[0])
