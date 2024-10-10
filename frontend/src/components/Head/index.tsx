import styled from "styled-components";
import { useContext, useState } from "react";
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
    padding: 5px 10px 0 10px;
    background-color: transparent
`

const DropdownContainer = styled.section`
    display: flex;
    align-items: center;
    position: relative;
    margin-left: auto;
    align-self: stretch;
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
    
    return (
        <HeaderElement>
            <nav>
                <HeaderUL>
                    <NavLi className="img">
                        <ImageLink to="/">
                            <IMG src={Logo}/>
                        </ImageLink>
                    </NavLi>
                    {user?
                        <DropdownContainer>
                            <div>
                                <div></div>
                                <div></div>
                                <div></div>
                            </div>
                            <DropdownUL>
                                <li><a href="{% url 'configurations' %}">Configurations</a></li>
                                <li><a href="{% url 'logout' %}">Logout</a></li>
                            </DropdownUL>
                        </DropdownContainer>
                    :
                        <NavLi>
                            <NavLink to="/login">Login</NavLink>
                        </NavLi>
                    }   
                </HeaderUL>
            </nav>
        </HeaderElement>
    )
    
}

export default Header