import styled from "styled-components";
import { useContext } from "react";
import { UserContext } from "../../main";
import FeedBacks from "../../components/FeedBacks";


function Home() {

    const [user,setUser] = useContext(UserContext)

    return (
            <main>
                <section className="introduction">
                    <div>
                        <h1>Câmbio Express</h1>
                        <p>Bem vindo{user? <span>{user.username}</span>:null} à maior agência de câmbio do país, onde você encontra:</p>
                        <ul>
                            <li>
                                <strong>Taxas Competitivas:</strong>
                                <p>
                                Oferecemos as melhores taxas de câmbio do mercado, garantindo que você obtenha o máximo valor pelo seu dinheiro.
                                </p>
                            </li>
                            <li>
                                <strong>Transações Seguras:</strong>
                                <p>
                                Utilizamos tecnologia avançada para garantir a segurança de todas as suas transações e proteger seus dados.
                                </p>
                            </li>
                            <li>
                                <strong>Plataforma Online Intuitiva:</strong>
                                <p>
                                Oferecemos uma plataforma digital fácil de usar para que você possa consultar taxas, fazer transações e monitorar seu saldo a qualquer hora e de qualquer lugar.
                                </p>
                            </li>
                            <li>
                                <strong>Variedade de Moedas:</strong>
                                <p>
                                Disponibilizamos uma ampla gama de moedas estrangeiras para que você possa realizar suas operações com facilidade, independentemente do destino.
                                </p>
                            </li>
                        </ul>
                    </div>
                    <div className="imgcontainer">
                        <img src=""/>
                        <section className="buttons">
                            <button>
                                Dólar
                                <input type="hidden" value="USD"/>
                            </button>
                            <button>
                                Euro
                                <input type="hidden" value="EUR"/>
                            </button>
                            <button>
                                Bitcoin
                                <input type="hidden" value="BTC"/>
                            </button>
                        </section>
                    </div>
                </section>

                <FeedBacks/>
        </main>
    )
}


export default Home
