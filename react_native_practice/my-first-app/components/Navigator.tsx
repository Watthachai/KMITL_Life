import { createStackNavigator } from '@react-navigation/stack';

/*import MainMenu from './screen/home';
import LoginScreen from './screen/login';
import RegisterScreen from './screen/register';
import RoomDetail from './screen/roomDetail';
import RoomBooked from './screen/roomBooked';
import RoomBooking from './screen/roomBooking';*/

import HomeScreen from '@/app/index';

const Stack = createStackNavigator();

const MyNavigator = () => {
return (
    <Stack.Navigator>
            <Stack.Screen name="index" component={ HomeScreen } options={{ headerShown: false }}/>
    </Stack.Navigator>
);
};

export default MyNavigator;