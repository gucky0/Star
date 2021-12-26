import 'package:flutter/material.dart';

void main() {
 runApp(MyANavBarScreen1());
}

class MyNavBarScreen1 extends StatelessWidget {
	@override
	Widget build(BuildContext context) {
		return MaterialApp(
			debugShowCheckedModeBanner: false,
			home: HomePage(),
		);
	}
}

class HomePage extends StateWidget {
	@override
	HomePageState createState() => HomePageState();
}

class HomePageState extends State<HomePage> {
	int selectedIndex = 0;
	List<IconData> data = [
		Icons.home_outlined,
		Icons.search,
		Icons.add_box_outlined,
		Icons.favorite_outline_sharp,
		Icons.person_outline_sharp
	];
	@override
	Widget build(BuildContext context) {
		return Scaffold(
			backgroundColor: Colors.greenAccent,
				padding: const EdgeInsets.all(20),
				child: Material(
					elevation: 10,
					borderRadius: BorderRadius.circular(20),
					color: Colors.black,
					child: Container(
						height: 70,
						width: double.infinity,
						child: ListView.builder(
							itemCount: data.length,
							padding: EdgeInsets.symmetric(horizontal: 10),
							itemBuilder: (ctx,i)=> Padding(
								padding: const EdgeInsets.symmetric(horizontal: 10),
								child: GestureDetector(
									onTap: (){
										setState(() {
											selectedIndex = i;
										});
									},
									child: AnimatedContainer(
										duration: Duration(
											milliseconds: 250
										),
										width: 35,
										decoration: BoxDecoration(
											border: i== selectedIndex 
												? Border(
													top: BorderSide(
														width:3,0,color:Colors.white))
												:null,
												gradient: LinearGradient(
													colors: [
														Colors.grey.shade800,
														Colors.black
													],
													begin: Alignment.topCenter,
													end: Alignment.bottomCenter
												)
												)
										),
										),
									),
								)),
					),
				),
			),
		);
	}