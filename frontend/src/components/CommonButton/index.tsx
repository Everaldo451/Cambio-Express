import React, { ButtonHTMLAttributes, StyleHTMLAttributes } from "react";
import styled from "styled-components";

interface CommonStyleProps {
    borderColor: React.CSSProperties['borderColor'],
    color: React.CSSProperties['color'],
    hoverColor: React.CSSProperties['color'],
    hoverBg: React.CSSProperties['backgroundColor'],
}

export const StyledButton = styled.button<{
        borderColor:CommonStyleProps['borderColor'], 
        color:CommonStyleProps['borderColor'],
        hoverColor: CommonStyleProps['hoverColor'],
        hoverBg:CommonStyleProps['hoverBg']
    }>`
    padding: 5px 10px;
    border: 1px solid ${(props) => props.borderColor};
    background-color: inherit;
    color:${(props) => props.color};
    transition: all 0.5s;

    &:hover {
        cursor: pointer;
        border: 1px solid transparent;
        background-color: ${(props) => props.hoverBg};
        color:${(props) => props.hoverColor};
    }
`

export const StyledInput = styled.input<{
        borderColor:CommonStyleProps['borderColor'], 
        color:CommonStyleProps['borderColor'],
        hoverColor: CommonStyleProps['hoverColor'],
        hoverBg:CommonStyleProps['hoverBg']
    }>`
    padding: 5px 10px;
    border: 1px solid ${(props) => props.borderColor};
    background-color: inherit;
    color:${(props) => props.color};
    transition: all 0.5s;

    &:hover {
        cursor: pointer;
        border: 1px solid transparent;
        background-color: ${(props) => props.hoverBg};
        color:${(props) => props.hoverColor};
    }
`

export default CommonStyleProps