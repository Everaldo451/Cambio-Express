import styled from "styled-components";
import React, { useContext, useState } from "react";
import { UserContext } from "../../main";
import { Link } from "react-router-dom";
import Logo from "../../assets/logo.png"

const HeaderElement = styled.header`
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
`

const HeaderUL = styled.ul`
    display: flex;
    margin: 0;
    list-style: none;
    align-items: center;
    padding: 0 10px 0 10px;
    background-color: transparent
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
        content: "";
        position: absolute;
        left: 50%;
        bottom: 0;
        height: 2px;
        background-color: rgb(202, 132, 2);
        width: 0;
        transition: all 0.5s;
    }

    &:nth-child(n+2) a:hover::after{
        left: 0;
        width: 100%;
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
`


function Header() {

    const [user,setUser] = useContext(UserContext)

    async function logoutFunc(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        e.preventDefault()

        try {

            const response = await fetch("http://localhost:8000/auth/logout",{
                method:"GET",
                credentials:"include"
            })

            if (response.redirected) {window.location.assign(response.url)}
        }
        catch(e) {window.location.assign("/")}
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