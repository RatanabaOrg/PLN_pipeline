import { useState } from 'react';
import { toast } from 'react-toastify';

export default function App() {
  const [url, setUrl] = useState('');

  async function cadastrarUrl(e) {
    e.preventDefault();

    if (url === '') {
      toast.error('Você deve fornecer a url!');
    } else {
      toast.success('URL enviada');
    }

    setUrl('');
  }

  return (
    <>
      <div className="content">

        <div className="container">
          <form className="forms">
            <label>Digite uma URL abaixo:</label>
            <input type="text" placeholder="URL" value={url} onChange={(e) => setUrl(e.target.value)} />
            <button className="submit" onClick={cadastrarUrl}>Enviar</button>
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
            <tr>
              <td data-label="Entrada">{url}</td>
              <td data-label="Saída">...textos...</td>
              <td data-label="Etapa">Raspagem</td>
              <td data-label="Tempo">5ms</td>
            </tr>
          </tbody>
        </table>

      </div>
    </>
  );
}