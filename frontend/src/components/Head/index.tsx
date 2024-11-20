import styled from "styled-components";
import React, { useContext, useMemo, useState} from "react";
import { UserContext } from "../../main";
import { Link, useNavigate } from "react-router-dom";
import Logo from "../../assets/logo.png"

const HeaderElement = styled.header`
    position: fixed;
    top: 0;
    left: 0;
    font-family: InstrumentSans;
    width: 100%;
    z-index: 2;
    box-shadow: 0 0 3px gray;
`

const HeaderUL = styled.ul`
    display: flex;
    margin: 0;
    list-style: none;
    align-items: center;
    padding: 5px 10px;
    background-color: #D9D9D9;
    backdrop-filter: blur(10px);
`

const DropdownContainer = styled.section`
    display: flex;
    align-items: center;
    position: relative;
    margin-left: auto;
    align-self: stretch;

    &:hover ul {
        display:flex;
    }
`

const DropdownButton = styled.button`
`

const GridDiv = styled.div`
    width: 30px;
    height: 60%;
    display: grid;
    gap: 4px;
    grid-auto-rows: 1fr;

    & div {
        background-color: black;
    }
`

const DropdownUL = styled.ul`
    position: absolute;
    display: none;
    flex-direction: column;
    padding: 0;
    right: 0;
    top: 100%;
    list-style: none;
    background-color: black;
`   

const DropdownLi = styled.li`
    padding: 10px;

    & a, button {
        background-color: black;
        border: none;
        display: block;
        width: 100%;
        color: white;
        text-decoration: none;
        text-align: center;
        font-size: 15px;

        &:hover {
            cursor: pointer;
        }
    }
`

const NavLi = styled.li`

    &:last-child{
        margin-left: auto;
    }

    &:nth-child(n+2) a::after{
        
    }

    &:nth-child(n+2) a:hover::after{
        
    }
`


const NavLink = styled(Link)`
    position: relative;
    display: block;
    color: black;
    text-decoration: none;
    padding: 5px 8px;
`

const ImageLink = styled(NavLink)`
    padding: 0;
`

const IMG = styled.img`
    height: 30px;
    display: block;
`


function Header() {

    const [user,setUser] = useContext(UserContext)
    const navigate = useNavigate()

    async function logoutFunc(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        e.preventDefault()

        try {

            const response = await fetch("/api/auth/logout/",{
                method:"GET",
                credentials:"include"
            })

            if (response.redirected) {navigate("/")}
        }
        catch(e) {navigate("/")}
    }
    
    return (
        <HeaderElement>
            <nav>
                <HeaderUL>
                    <NavLi className="img">
                        <ImageLink to={"/"}>
                            <IMG src={Logo}/>
                        </ImageLink>
                    </NavLi>
                    {user?
                        <DropdownContainer>
                            <GridDiv>
                                <div></div>
                                <div></div>
                                <div></div>
                            </GridDiv>
                            <DropdownUL>
                                <DropdownLi>
                                    <Link to="/configurations">Configurations</Link>
                                </DropdownLi>
                                <DropdownLi>
                                    <Link to="/investiments">Investiments</Link>
                                </DropdownLi>
                                <DropdownLi>
                                    <button onClick={logoutFunc}>Logout</button>
                                </DropdownLi>
                            </DropdownUL>
                        </DropdownContainer>
                    :
                        <NavLi>
                            <NavLink to={"/login"}>Login</NavLink>
                        </NavLi>
                    }   
                </HeaderUL>
            </nav>
        </HeaderElement>
    )
    
}

export default Header