import { useState } from 'react';
import { toast } from 'react-toastify';
import axios from 'axios'; // Import axios

export default function App() {
  const [url, setUrl] = useState('');

  async function cadastrarUrl(e) {
    e.preventDefault();

    if (url === '') {
      toast.error('Você deve fornecer a URL!');
      return; // Add a return statement to prevent further execution
    } 


    var responde = await axios.post('http://127.0.0.1:5000/process', { route: url }); 
    var data = responde.data
    console.log(data);
    
    toast.success('URL enviada');

    setUrl(''); // Clear the input field
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
            <button className="submit" type="submit">Enviar</button> {/* Changed to type="submit" */}
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
