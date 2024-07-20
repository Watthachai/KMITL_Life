
import React from "react";
import {StyleSheet, View, Text, TouchableOpacity} from "react-native";
import { colors } from "@/components/Colors";
import { Button } from "react-native";
import { NavigationContainer } from '@react-navigation/native';



export default function HomeScreen() {
    const onLogin = () => {
        /*navigation.navigate('login');*/
    };

    return (
        /*<View style={style.container}>
            <View style = {{padding: 30}}>
                <Text style = {style.text}>     Meety</Text>
                <Text style = {style.text}>
                    Meeting Me
                </Text>
            </View>
            <View style = {[style.box]}></View>
            <TouchableOpacity style={style.btnConfirm} onPress={onLogin}>
                <Text style={{color: colors.white, fontSize: 16}}>Let's get started!</Text>
            </TouchableOpacity>
        </View>*/
      <View style={{flex: 1}}>
      <View style={{flex: 5, backgroundColor: 'powderblue'}} />
      <View style={{flex: 1, backgroundColor: 'skyblue'}} />
    </View>
    );
}
const style = StyleSheet.create({
        container: {
            flex: 1,
            backgroundColor: colors.secondary,
            alignItems: "center",
            justifyContent: "center",
        },
        text: {
            fontSize: 32,
            fontWeight: "bold",
            color: colors.dark,
        },
        box: {
            width: 200,
            height: 200,
            backgroundColor: colors.box,
            borderRadius: 20
        },
        btnConfirm: {
            position: "absolute",
            bottom: 80, // ...at the bottom of its container
            left: 30,
            right: 30,
            backgroundColor: '#31393C', // light grey background
            flexDirection: "row",
            justifyContent: "center", // center the content
            alignItems: "center",
            padding: 0, // some padding
            paddingBottom: 10, // add safe area padding to existing padding
            elevation: 10, // shadow for Android
            shadowColor: '#000', // shadow for iOS
            shadowOffset: { width: 0, height: 2 },
            shadowOpacity: 0.25,
            shadowRadius: 3.84,
            paddingHorizontal: 20,
            paddingVertical: 20,
            borderRadius: 10,
        },
    })
