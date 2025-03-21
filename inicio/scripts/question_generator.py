from groq import Groq
import json
import pandas as pd
from .baseModels import QuestionSet
import fitz


class QuestionGenerator:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def get_questions_from_text(self, text: str) -> QuestionSet:
        """Gera questões a partir de um texto usando a API do Groq."""

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                    "role": "system",
                    "content": (
                        "Sempre em português brasileiro. "
                        "Crie 5 perguntas a partir do texto fornecido. "
                        "A resposta deve ser no formato JSON seguindo o schema: "
                        f"{QuestionSet.model_json_schema()}"
                        "- Deve ter 5 alternativa em cada questão."
                        "- Caso seja uma questão de verdadeiro ou falso pode ser 2 alternativas. Uma delas tem que conter Verdadeiro como texto e a outra Falso"
                        "- Não esqueça de colocas a explicação de cada questão."
                        "- Tente ao máximo colocar somente 1 questão de verdadeiro ou falso."
                        "- A explicação do porquê uma questão ser errada deve ser bem detalhada, assim como a de ser correta, mas não coloque um texto muito extenso."
                    )
                },
                {
                    "role": "user",
                    "content": text,
                }
            ],
            model="llama3-70b-8192",
            response_format={"type": "json_object"},
            )

            return QuestionSet.model_validate_json(
                chat_completion.choices[0].message.content
            )
        
        except Exception as e:
            raise Exception(f"a IA não conseguiu gerar as questões, tente novamento dentro de alguns instantes.")
    
    def extract_text_from_pdf(self, pdf_file):
        try:
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")  # Abre o arquivo PDF a partir do objeto de arquivo
            text = ""
            for page in doc:
                text += page.get_text("text") + "\n"
            return text
        except Exception as e:
            raise Exception(f"Não foi possível extrair os dados do PDF, tente novamente em alguns instantes.")

    def print_questions(self, question_set: QuestionSet):
        """Imprime as questões formatadas."""
        try:
            for i, question in enumerate(question_set.questions):
                print(f"\nQuestão {i}:")
                print(question.question_text)
        except Exception as e:
            raise Exception(f"causado em print_questions - {e}")

    def save_questions_to_file(self, question_set: QuestionSet, filename: str):
        """Salva as questões em um arquivo JSON."""
        try:

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(question_set.dict(), file, ensure_ascii=False, indent=4)
                print(f"Questões salvas em {filename}")

        except Exception as e:
            raise Exception(f"Não foi possível salvar as questões em um arquivo JSON, tente novamente em alguns instantes.")

    def json_to_dataframe(self, json_file_path: str) -> pd.DataFrame:
        try:
            # Carrega o arquivo JSON
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Lista para armazenar os dados formatados
            flat_data = []

            # Processa cada questão
            for question in data['questions']:
                # Encontra a alternativa correta
                correct_alt = next(alt for alt in question['alternatives'] if alt['is_correct'])
                
                # Cria o dicionário base com a questão
                question_dict = {
                    'question_text': question['question_text'],
                    'correct_answer': correct_alt['text'],
                    'explanation': correct_alt['explanation']
                }
                
                # Adiciona todas as alternativas dinamicamente
                for i, alt in enumerate(question['alternatives']):
                    letter = chr(97 + i).upper()  # Converte 0->A, 1->B, 2->C, etc.
                    question_dict[f'alternative_{letter}'] = alt['text']
                    question_dict[f'is_correct_{letter}'] = alt['is_correct']
                    question_dict[f'explanation_{letter}'] = alt['explanation']
                
                flat_data.append(question_dict)
            
            # Cria o DataFrame
            df = pd.DataFrame(flat_data)
            
            return df
        
        except FileNotFoundError:
            raise Exception(f"Arquivo {json_file_path} não encontrado.")
        except json.JSONDecodeError:
            raise Exception(f"O arquivo {json_file_path} não é um JSON válido.")
        except Exception as e:
            raise Exception(f"Erro inesperado: {str(e)}")
