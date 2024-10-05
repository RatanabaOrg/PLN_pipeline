import { useState } from 'react';
import { toast } from 'react-toastify';
import axios from 'axios'; // Import axios

export default function App() {
  const [url, setUrl] = useState('');
  const [data, setData] = useState(null); // Initialize data as null

  async function cadastrarUrl(e) {
    e.preventDefault();

    if (url === '') {
      toast.error('Você deve fornecer a URL!');
      return; // Add a return statement to prevent further execution
    }

    try {
      const response = await axios.post('http://127.0.0.1:5000/process', { route: url });
      setData(response.data); // Set the received data
      toast.success('URL enviada');
    } catch (error) {
      toast.error('Erro ao enviar URL!');
      console.error('Error:', error); // Log error for debugging
    } finally {
      setUrl(''); // Clear the input field
    }
  }

  return (
    <>
      <div className="content">
        <div className="container">
          <form className="forms" onSubmit={cadastrarUrl}>
            <label>Digite uma URL abaixo:</label>
            <input
              type="text"
              placeholder="URL"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
            <button className="submit" type="submit">Enviar</button>
          </form>
        </div>

        <table>
          <thead>
            <tr>
              <th scope="col">Entrada</th>
              <th scope="col">Saída</th>
              <th scope="col">Etapa</th>
              <th scope="col">Tempo</th>
            </tr>
          </thead>
          <tbody>
            {data && data.scraping && (
              <tr>
                <td data-label="Entrada">{data.scraping.entry}</td>
                <td data-label="Saída">{data.scraping.exit}</td>
                <td data-label="Etapa">Raspagem</td>
                <td data-label="Tempo">{data.scraping.time}</td>
              </tr>
            )}
            {data && data.cleaned_word_1 && (
              <tr>
                <td data-label="Entrada">{data.cleaned_word_1.entry}</td>
                <td data-label="Saída">{data.cleaned_word_1.exit}</td>
                <td data-label="Etapa">Remoção de Ruído</td>
                <td data-label="Tempo">{data.cleaned_word_1.time}</td>
              </tr>
            )}
            {data && data.tokenized_sentences && (
              <tr>
                <td data-label="Entrada">{data.tokenized_sentences.entry}</td>
                <td data-label="Saída">{data.tokenized_sentences.exit}</td>
                <td data-label="Etapa">Tokenização de Frases</td>
                <td data-label="Tempo">{data.tokenized_sentences.time}</td>
              </tr>
            )}
            {data && data.tokenized_words && (
              <tr>
                <td data-label="Entrada">{data.tokenized_words.entry}</td>
                <td data-label="Saída">{data.tokenized_words.exit}</td>
                <td data-label="Etapa">Tokenização de Palavras</td>
                <td data-label="Tempo">{data.tokenized_words.time}</td>
              </tr>
            )}
            {data && data.cleaned_word_2 && (
              <tr>
                <td data-label="Entrada">{data.cleaned_word_2.entry}</td>
                <td data-label="Saída">{data.cleaned_word_2.exit}</td>
                <td data-label="Etapa">Limpeza de Tokense e Conversão para Minúsculos</td>
                <td data-label="Tempo">{data.cleaned_word_2.time}</td>
              </tr>
            )}
            {data && data.replaced_abbreviations && (
              <tr>
                <td data-label="Entrada">{data.replaced_abbreviations.entry}</td>
                <td data-label="Saída">{data.replaced_abbreviations.exit}</td>
                <td data-label="Etapa">Substituição de Abreviações</td>
                <td data-label="Tempo">{data.replaced_abbreviations.time}</td>
              </tr>
            )}
            {data && data.correct_words && (
              <tr>
                <td data-label="Entrada">{data.correct_words.entry}</td>
                <td data-label="Saída">{data.correct_words.exit}</td>
                <td data-label="Etapa">Correção de Caracteres Incorretos</td>
                <td data-label="Tempo">{data.correct_words.time}</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </>
  );
}
